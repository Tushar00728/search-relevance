
def matchingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:

            if word1.lower() == word2.lower():
                score +=1
    return score


if __name__=="__main__":

    sentences = ["python is a language", "python snake", "Elon musk is the goat"]

    search = input("Enter your query\n")

    relScores = [matchingWords(search,sentence) for sentence in sentences]

    sortedrelScores = [relscore for relscore in sorted(
        zip(relScores,sentences), reverse = True) if relscore[0] != 0]

    print(f"{len(sortedrelScores)} results found!")
    for score, item in sortedrelScores:
        print(f"\"{item}\": with a score of {score}") 
