cd veggie-favorites

git add chili.txt

git add squash-lasagna.txt
			
git commit -m "Added some changes in chili and lasagna."

cd ../veggie-clone

git fetch

git merge origin/master

git branch try-recipe
			
git checkout try-recipe

git add new-recipe.txt
			
git commit -m "Added my fav meals."

git fetch

git push origin try-recipe

cd ../veggie-favorites

git branch

git checkout try-recipe

