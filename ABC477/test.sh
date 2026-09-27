while true; do
    python3 '/Users/tsukasa-tanaka/projects/ABC/ABC477/gen.py' > input.txt
    ans1=$(python3 '/Users/tsukasa-tanaka/projects/ABC/ABC477/E.py' < input.txt)
    ans2=$(python3 '/Users/tsukasa-tanaka/projects/ABC/ABC477/E_ans.py' < input.txt)
    if [ $ans1 != $ans2 ]; then
        echo "Wrong Answer"
        echo $ans1
        echo $ans2
        exit
    fi
done