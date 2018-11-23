git add .
git commit -m "first try for set temperature"
git push origin master 
cd ../mycroft-skills
git pull
git submodule update --remote skill-klima
git add skill-klima
git commit -m "update klima"
git push origin 18.08
cd ../skill-klima
ssh mycorf@10.0.200.216 './mycroft-core/bin/mycroft-msm -u https://github.com/HackYourOffice/mycroft-skills update skill-klima'
