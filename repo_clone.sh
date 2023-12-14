#!/bin/bash

# List of Git repositories to clone
repositories=(
  "https://github.com/jfinal/jfinal.git"
)

# Destination directory where repositories will be cloned
destination_directory="~/project/SemanticLifter/EmpiricalStudy/dataset/"

# Loop through each repository and clone it
for repo in "${repositories[@]}"; do
  repo_name=$(basename "$repo" .git)
  destination_path="$destination_directory/$repo_name"

  echo "Cloning $repo into $destination_path"
  git clone "$repo" "$destination_path"
done

echo "Cloning complete"
