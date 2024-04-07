import difflib

def compare_strings(str1, str2):
    # Create a SequenceMatcher object with the two strings
    seq_matcher = difflib.SequenceMatcher(None, str1, str2)
    
    # Get the ratio of similarity as a float
    similarity_ratio = seq_matcher.ratio()
    
    # Convert the ratio to a percentage
    similarity_percentage = similarity_ratio * 100
    
    # Return the similarity percentage
    return similarity_percentage