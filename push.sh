git add .
git commit -m "$2"
git push origin master 
cd ../mycroft-skills
git pull
git submodule update --remote skill-$1
git add skill-$1
git commit -m "update $1"
git push origin 18.08
cd -
ssh mycorf@10.0.200.216 "./mycroft-core/bin/mycroft-msm -u https://github.com/HackYourOffice/mycroft-skills update skill-$1"
