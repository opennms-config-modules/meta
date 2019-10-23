for /D %%G in (C:\SW-Projekte\meta_2\*) do (
cd %%G
git add -A
git commit -m "fix IndexStorageStrategy and PersistAllSelectorStrategy class path"
git push origin master
cd ..
)

