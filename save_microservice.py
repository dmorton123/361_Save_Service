"""
Save Microservice - Handles all game save/load operations
Run separately from the main game application
"""

from flask import Flask, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)

# Configure save directory
SAVE_DIR = Path(__file__).parent / "saves"
SAVE_DIR.mkdir(exist_ok=True)

def error_response(e, status=500):
    return jsonify({
        "success": False,
        "error": str(e)
    }), status

@app.route('/save', methods=['POST'])
def save_game():
    """
    Save any dictionary to file
    
    Expected JSON payload:
    {
        "data": { any dictionary structure },
        "filename": str (optional, defaults to "autosave.json")
    }
    """
    try:
        payload = request.get_json()
        # Validate required fields
        if not payload or "data" not in payload:
            return jsonify({
                "success": False,
                "error": "Missing required field: 'data'"
            }), 400
        
        # Get filename, default to autosave
        filename = payload.get("filename", "autosave.json")
        filepath = SAVE_DIR / filename
        
        # Write to file
        with open(filepath, "w") as f:
            json.dump(payload["data"], f, indent=2)
        
        return jsonify({
            "success": True,
            "message": f"Game saved successfully to {filename}",
            "filepath": str(filepath)
        }), 200
        
    except Exception as e:
        return error_response(e, 500)

@app.route('/load/<filename>', methods=['GET'])
def load_game(filename):
    """
    Load game state from file
    
    Args:
        filename: Name of the save file (e.g., 'savegame.json')
    """
    try:
        filepath = SAVE_DIR / filename
        
        if not filepath.exists():
            return jsonify({
                "success": False,
                "error": f"Save file '{filename}' not found"
            }), 404
        
        # Read file
        with open(filepath, "r") as f:
            data = json.load(f)
        
        return jsonify({
            "success": True,
            "data": data
        }), 200

    except Exception as e:
        return error_response(e, 500)

@app.route('/list-saves', methods=['GET'])
def list_saves():
    """List all available save files"""
    try:
        saves = []
        for save_file in SAVE_DIR.glob("*.json"):
            saves.append({
                "filename": save_file.name,
            })
        
        return jsonify({
            "success": True,
            "saves": saves
        }), 200
        
    except Exception as e:
        return error_response(e, 500)

if __name__ == '__main__':
    print(f"Save Microservice running on http://localhost:5000")
    print(f"Saves directory: {SAVE_DIR.absolute()}")
    app.run(debug=False, host='localhost', port=5000)
