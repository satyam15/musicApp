from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('normalized_data.csv')

data = df.to_dict(orient='records')

@app.route('/songs', methods=['GET'])
def get_songs():
    # Implement pagination
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start = (page - 1) * per_page
    end = start + per_page
    
    return jsonify(data[start:end])

@app.route('/song/<title>', methods=['GET'])
def get_song_by_title(title):
    song = next((item for item in data if item['title'].lower() == title.lower()), None)
    if song:
        return jsonify(song)
    return jsonify({'message': 'Song not found'}), 404

@app.route('/song/<title>/rate', methods=['POST'])
def rate_song(title):
    song = next((item for item in data if item['title'].lower() == title.lower()), None)
    if song:
        rating = request.json.get('rating')
        if 1 <= rating <= 5:
            song['star_rating'] = rating
            return jsonify({'message': 'Rating updated'}), 200
        return jsonify({'message': 'Rating should be between 1 and 5'}), 400
    return jsonify({'message': 'Song not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

