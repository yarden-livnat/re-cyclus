#!/usr/bin/env bash

declare -a swarm=('vm1' 'vm2' 'vm3' 'vm4')

for machine in "${swarm[@]}"
do
    echo "$machine"
    if [[ `docker-machine status $machine` ]]; then
        echo "yes"
    else
       echo "no"
    fi
done
