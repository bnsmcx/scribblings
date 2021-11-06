#!/bin/bash

for i in {7..20}
    do
        for j in {0..20}
            do
                for k in {0..20}
                    do
                        echo https://www.gstatic.com/firebasejs/$i.$j.$k/firebase-auth.js
                    done
            done
    done

