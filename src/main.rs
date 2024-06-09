use std::fs;
use std::str::Lines;

fn main() {
    // --snip--
    let file_path = "src/static/sa/agency.txt";
    println!("In file {}", file_path);

    let file_contents = fs::read_to_string(file_path)
        .expect("File read should be successful.");

    let line_iterator: Lines = file_contents.lines();

    for line in line_iterator {
        line_splitter(line);
    }
}

fn line_splitter(line: &str) {
    let term = line.split(",");
    let variable: Vec<&str> = term.collect();
    dbg!(variable);
}
