import spacy

# Load the en_core_web_md model
nlp = spacy.load("en_core_web_md")

# Read in the movies.txt file
with open("movies.txt", "r") as f:
    movies = f.readlines()

# Define a function to find related movies
def find_related_movies(movie_title, movie_description, movies):
    # Process the movie description using spaCy
    doc = nlp(movie_description)
    
    # Extract the keywords from the movie description
    keywords = [token.lemma_ for token in doc if token.pos_ in ["NOUN", "ADJ"]]
    
    # Create an empty list to store related movies
    related_movies = []
    
    # Loop through all the movies and find related movies
    for movie in movies:
        # Skip the current movie if it is the same as the input movie
        if movie_title.lower() in movie.lower():
            continue
        
        # Process the movie using spaCy
        movie_doc = nlp(movie)
        
        # Check if any of the keywords from the movie description are in the movie
        if any(keyword in movie_doc.text.lower() for keyword in keywords):
            # If a keyword is found, add the movie to the list of related movies
            movie_title = movie.split(" (")[0]
            related_movies.append(movie_title)
    
    # Return the list of related movies
    return related_movies

# Example usage
movie_title = "Planet Hulk"
movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator"
related_movies = find_related_movies(movie_title, movie_description, movies)

# Print each related movie on a separate line
print("Related movies:")
for movie in related_movies:
    print(movie)

# Extract the movie titles from each related movie
movie_title = related_movies[0].split(":")[0].strip()

# Print the movie title
print("Movie title:", movie_title)
