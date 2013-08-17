#!/bin/bash
set -e

root_src="sdjl@lengxiaohua3:/opt/lengxiaohua_discuz/"
root_dst="/home/sdjl/backup/lengxiaohua_discuz/"
options=(-avzcsP --delete-excluded -e "ssh -p 22 -l sdjl")

sub_paths=(/ )
excludes=()
rotate_count=7

for i in ${!sub_paths[@]}; do
    sub_paths[$i]="$root_src/./${sub_paths[$i]}"
done

for i in ${!excludes[@]}; do
    excludes[$i]="--filter=-s ${excludes[$i]}"
done

if [ ! -d "$root_dst" ]; then
    mkdir "$root_dst"
fi

rsync "${options[@]}" "${excludes[@]}" "${sub_paths[@]}" "$root_dst/"

bak_path=$(echo "$root_dst" | sed 's|/*$||')
for i in $(eval echo {1..$rotate_count}); do
    rotate_count=$i
    if [ ! -d "$bak_path.$i" ]; then
        break
    fi
done

rm -r "$bak_path.$rotate_count" 2>/dev/null || true

for ((i=$rotate_count;i>1;i--)); do
    mv "$bak_path.$(($i - 1))" "$bak_path.$i"
done

cp -r "$bak_path" "$bak_path.1"
