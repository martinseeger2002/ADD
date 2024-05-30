# Anti Doginal Dogs (ADD)

This repository contains the data for the Anti Doginal Dogs (ADD) project. Each dog in the collection has a set of traits and values that need to be updated from [doggy.market](https://doggy.market/nfts/doginaldogs).

## How to Update the JSON File

1. **Fork the Repository**:
   - Go to the [original repository](https://github.com/martinseeger2002/ADD).
   - Click on the "Fork" button in the top right corner to create your own copy of the repository.

2. **Download the JSON File**:
   - Navigate to the `Anti_Doginal_Dogs.json` file in your forked repository.
   - Download the JSON file to your local machine for editing. (GitHub might not allow direct edits due to the file size).

3. **Find the Traits and Values**:
   - Visit [doggy.market/nfts/doginaldogs](https://doggy.market/nfts/doginaldogs).
   - Find the corresponding dog number and gather the traits and values (Background, Fur Color, Fur Pattern, Head, Clothes, Mouth, Eyes, Accessory, txid).

4. **Update the JSON File**:
   - Open the downloaded `Anti_Doginal_Dogs.json` file with a text editor.
   - Locate the entry for the dog you want to update.
   - Fill in the corresponding traits and values. Here is an example:

     ```json
     [
         {
             "name": "Anti Dog #1",
             "traits": {
                 "Background": "Sky Blue",
                 "Fur Color": "Brown",
                 "Fur Pattern": "Spotted",
                 "Head": "Top Hat",
                 "Clothes": "Tuxedo",
                 "Mouth": "Smile",
                 "Eyes": "Blue",
                 "Accessory": "Bow Tie",
                 "txid": "123abc456def"
             }
         },
         ...
     ]
     ```

5. **Upload the Updated JSON File**:
   - Save the changes to the `Anti_Doginal_Dogs.json` file.
   - Upload the updated JSON file back to your forked repository. Replace the old file with the new one.

6. **Create a Pull Request**:
   - Go to your forked repository on GitHub.
   - Click on "Pull requests" then "New pull request".
   - Ensure that the base repository is `martinseeger2002/ADD` and the base branch is `main`.
   - Provide a clear title and description for your pull request, explaining the updates you made.
   - Submit the pull request.

7. **Avoid Duplicate Inscriptions**:
   - Before submitting your pull request, check the open pull requests in the [original repository](https://github.com/martinseeger2002/ADD/pulls) to ensure that no one else has already updated the same dog entry.
   - If someone else has already updated the dog, do not submit a duplicate update.

## Minting Instructions

If you need assistance with minting, indicate this in your pull request. Someone from the community will assist you with the minting process to ensure there are no duplicate inscriptions.

## Important Notes

- Ensure that all information is accurate and corresponds to the data from [doggy.market/nfts/doginaldogs](https://doggy.market/nfts/doginaldogs).
- Collaborate and communicate with other contributors to avoid conflicts and duplicate entries.
- Regularly check the original repository for updates and new information.

Thank you for contributing to the Anti Doginal Dogs project!
