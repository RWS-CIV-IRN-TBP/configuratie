version=1.0.5
cd ~/apps/geoservices/apps/
rm -Rf kustlijnkaart
rm -Rf vegetatielegger
rm -Rf pdokkaart
svn export https://github.com/RWS-CIV-IRN-TBP/kustlijnkaart/trunk kustlijnkaart
svn export https://github.com/RWS-CIV-IRN-TBP/vegetatielegger/trunk vegetatielegger
svn export https://github.com/Geonovum/pdokkaart/trunk pdokkaart

cd ../../
rm -Rf /tmp/pdok-apps-$version
mkdir -p /tmp/pdok-apps-$version/apps/
cp -R geoservices/httpd.d /tmp/pdok-apps-$version/
cp -R geoservices/apps/pdokkaart /tmp/pdok-apps-$version/apps/
cp -R geoservices/apps/vegetatielegger /tmp/pdok-apps-$version/apps/
cp -R geoservices/apps/kustlijnkaart /tmp/pdok-apps-$version/apps/
cd /tmp
rm ~/redhat/SOURCES/pdok-apps-$version.tgz
tar -cvzf ~/redhat/SOURCES/pdok-apps-$version.tgz pdok-apps-$version/
