# Learning
A collection of miscellaneous learning materials and notes, mostly on technical topics for the software engineer. Topics are loosely separated by directories in the root of the project. The presence of an `exercises.toml` file within a topic directory means the information is quizzable - the project cli can be run to perform the exercises for practice. 

## Prequisites

1. Install Rust
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
Follow the default installation prompts and then reload your shell
```
source $HOME/.cargo/env
```
2. Clone and build
```
git clone https://github.com/wadeptr/learning.git
```
```
cd learning
```
```
cargo build --release
```

## Usage
The cli scans the working directory for subdirectories that contain `exercises.toml` and makes them available with hints through the interactive cli. 
```rust
cargo run           # interactive topic picker
cargo run -- vim    # skip to vim exercises
```

