while true; do
    python3 '/Users/tsukasa-tanaka/projects/ABC/ABC474/gen.py' > input.txt
    ans2=$(python3 '/Users/tsukasa-tanaka/projects/ABC/ABC475/E.py' < input.txt)
done