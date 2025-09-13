from flask import Flask, request, jsonify
from debate_engine.generator import ArgumentGenerator
from debate_engine.rebuttal import RebuttalEngine
from debate_engine.scorer import DebateScorer

app = Flask(__name__)
arg_gen = ArgumentGenerator()
rebuttal_gen = RebuttalEngine()
scorer = DebateScorer()

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    topic = data['topic']
    stance = data['stance']
    argument = arg_gen.generate_argument(topic, stance)
    score = scorer.score_relevance(argument, topic)
    return jsonify({'argument': argument, 'relevance_score': score})

@app.route('/rebuttal', methods=['POST'])
def rebuttal():
    data = request.json
    counter = data['counterargument']
    rebuttal = rebuttal_gen.generate_rebuttal(counter)
    return jsonify({'rebuttal': rebuttal})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
