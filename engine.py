class AnimeRating:
    def __init__(self, animation_quality, music, characters, character_development, story, plot,
                 entertainment, impact = None, immersion = None):
        self.animation_quality = animation_quality
        self.music = music
        self.characters = characters
        self.character_development = character_development
        self.story = story
        self.plot = plot
        self.entertainment = entertainment
        self.scores = [
            self.animation_quality, 
            self.music,
            self.characters,
            self.character_development,
            self.story,
            self.plot,
            self.entertainment
        ]
        if impact:
            self.impact = impact
            self.scores.append(self.impact)
        if immersion:
            self.immersion = immersion
            self.scores.append(self.immersion)

    def get_final_score(self):
        total = 0
        for value in self.scores:
            total += value
        score = (total / 80) * 10
        if int(str(score).split('.')[1]) == 0: return int(score)
        return score


class MovieRating(AnimeRating):
    def __init__(self, production_quality, music, characters, character_development, story, plot,
                 entertainment, impact = None, immersion = None):
        self.production_quality = production_quality
        self.music = music
        self.characters = characters
        self.character_development = character_development
        self.story = story
        self.plot = plot
        self.entertainment = entertainment
        self.scores = [
            self.production_quality, 
            self.music,
            self.characters,
            self.character_development,
            self.story,
            self.plot,
            self.entertainment
        ]
        if impact:
            self.impact = impact
            self.scores.append(self.impact)
        if immersion:
            self.immersion = immersion
            self.scores.append(self.immersion)


class TvShowRating(MovieRating):
    def __init__(self, production_quality, music, characters, character_development, story, plot,
                 entertainment, impact = None, immersion = None):
        super().__init__(production_quality, music, characters, character_development, story, plot,
                         entertainment, impact, immersion)
