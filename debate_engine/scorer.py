from sentence_transformers import SentenceTransformer, util

class DebateScorer:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def score_relevance(self, argument, topic):
        emb1 = self.model.encode(argument, convert_to_tensor=True)
        emb2 = self.model.encode(topic, convert_to_tensor=True)
        score = util.pytorch_cos_sim(emb1, emb2)
        return float(score[0][0])
