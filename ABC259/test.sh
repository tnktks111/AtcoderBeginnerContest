while true; do
    python3 '/Users/tsukasa-tanaka/projects/ABC/ABC259/gen.py' > input.txt
    ans1=$(python3 '/Users/tsukasa-tanaka/projects/ABC/ABC259/E - LCM on Whiteboard.py' < input.txt)
    ans2=$(python3 '/Users/tsukasa-tanaka/projects/ABC/ABC259/E_ans.py' < input.txt)
    if [ $ans1 != $ans2 ]; then
        echo "Wrong Answer"
        echo $ans1
        echo $ans2
        exit
    fi
done