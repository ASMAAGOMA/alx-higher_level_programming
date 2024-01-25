#!/bin/bash
#displays the size of the body of the response#
curl -s -o /dev/null "%{size_downloaded}"
