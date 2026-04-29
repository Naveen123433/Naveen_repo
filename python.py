echo "Creating Python file"

cat > hello.py << 'EOF'
print("Hello from Python")
print("Running Python script from Jenkins")

name = "JayathiSoft Student"
print("Welcome", name)
EOF

echo "Running Python script"
python3 hello.py
