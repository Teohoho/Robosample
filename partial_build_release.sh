##!/bin/bash
#
## remove openmm previous openmm compilation
#sudo rm /usr/local/openmm -rf
#sudo find /usr/local/lib -iname '*openmm*' -delete
#rm openmm/build-debug -rf
#rm openmm/build-release -rf
#
## delete previous simbody compilation from /usr/
#sudo rm /usr/local/lib/cmake/simbody -rf
#sudo rm /usr/local/lib/simbody -rf
#sudo rm /usr/local/lib/pkgconfig/simbody.pc
#sudo find /usr/local/lib -name 'libSimTK*' -delete
#
## compile openmm
#cd openmm
#mkdir build-release
#cd build-release/
#cmake -DCMAKE_BUILD_TYPE=Release ..
#make -j$((`nproc`*2))
#sudo make install
#cd ../../
#
## delete previous compilation from project
#cd Molmodel/Simbody01
#rm build-debug -rf
#rm build-release -rf
#
#cd ../
#rm build-debug -rf
#rm build-release -rf
#
#cd ../
#rm build-debug -rf
#rm build-release -rf
#
## compile project
#cd Molmodel/Simbody01
#mkdir build-release
#cd build-release
#cmake -DCMAKE_BUILD_TYPE=Release ..
#make -j$((`nproc`*2))
#sudo make install
#
#cd ../../
#mkdir build-release
#cd build-release
#cmake -DCMAKE_BUILD_TYPE=Release ..
#make -j$((`nproc`*2))
#sudo make install
#
## ensure this is correctly installed
#sudo mkdir -p /usr/local/lib/plugins/ && sudo cp -f libOpenMMPlugin.so $_
#rm /usr/local/lib/plugins/libOpenMMPlugin_d.so

#cd ../../
#mkdir build-release
#cd build-release
cmake -DCMAKE_BUILD_TYPE=Release .. 
make -j$((`nproc`*2))
sudo /sbin/ldconfig

# cmake -DCMAKE_BUILD_TYPE=Release -DROBO_PGO=Generate ..
# make -j$((`nproc`*2))
# sudo /sbin/ldconfig
# ./tests/Robosample inp
# cmake -DCMAKE_BUILD_TYPE=Release -DROBO_PGO=Profile ..
# make -j$((`nproc`*2))
# sudo /sbin/ldconfig

# add test input files
#cp -ri ../tests_inputs/* .
#mkdir temp
#mkdir temp/pdbs

# add tests
#cp ../tests/test-memory.sh test-memory.sh
