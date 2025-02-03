#!/bin/bash

current_time=$(date +"%H:%M")
end_time="18:00"

current_seconds=$(date -j -f "%H:%M" "$current_time" +%s)
end_seconds=$(date -j -f "%H:%M" "$end_time" +%s)

remaining_seconds=$((end_seconds - current_seconds))

if [ $remaining_seconds -lt 0 ]; then
    echo "Workday is over!"
else
    hours=$((remaining_seconds / 3600))
    minutes=$(( (remaining_seconds % 3600) / 60 ))

    echo "Current time: $current_time"
    echo "Workday ends in: $hours hours and $minutes minutes"
fi

















