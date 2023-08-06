#!/bin/bash
###########

export ARGS="$@"
espeak "$ARGS" 2> /dev/null

