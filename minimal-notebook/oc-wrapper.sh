#!/bin/bash

case $OC_VERSION in
    3.10|3.10+|3.10.*)
        OC_VERSION=3.10
        ;;
    3.11|3.11+|3.11.*)
        OC_VERSION=3.11
        ;;
    4.0|4.0+|4.0.*)
        OC_VERSION=4.0
        ;;
    4.1|4.1+|4.1.*)
        OC_VERSION=4.1
        ;;
    4.2|4.2+|4.2.*)
        OC_VERSION=4.2
        ;;
    4.3|4.3+|4.3.*)
        OC_VERSION=4.3
        ;;
    4.10|4.10+|4.10.*)
        OC_VERSION=4.10
        ;;
    4.11|4.11+|4.11.*)
        OC_VERSION=4.11
        ;;
    4.12|4.12+|4.12.*)
        OC_VERSION=4.12
        ;;
    *)
        OC_VERSION=4.12
        ;;
esac

exec /opt/app-root/bin/oc-$OC_VERSION "$@"
