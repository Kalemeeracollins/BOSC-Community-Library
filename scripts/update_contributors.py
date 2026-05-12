def update_contributors(new_names):
    # Existing list of contributors
    current_contributors = ["Kalema Kosea", "John Mark", "Lowi Smith"]
    
    # The BUG: Simply appending creates duplicates
    # current_contributors.extend(new_names) 

    # THE FIX: Use a set to enforce uniqueness
    unique_list = list(set(current_contributors + new_names))
    unique_list.sort() # Keep it professional by alphabetizing

    with open("CONTRIBUTORS.md", "w") as f:
        f.write("# Project Contributors\n\n")
        for name in unique_list:
            f.write(f"* {name}\n")

# Example usage that would have caused a bug:
update_contributors(["Kalema Kosea", "New Contributor"])