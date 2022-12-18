fn main() {
    let mut s = String::from("hello");
    s.push_str(", world!");
    let s2 = s.clone();
    let x = 5;
    takes_ownership(s2);
    makes_copy(x);

    // ownership already taken for s2
    //println!("x = {}, s = {}, s2 = {}", x, s, s2);

    let s3 = takes_ownership_and_gives_back(s);
    println!("{}", s3);

    let (s4, len) = calculate_len(s3); 
}

fn takes_ownership(some_string: String) {
    println!("{}", some_string);
}

fn makes_copy(some_integer: u32) {
    println!("{}", some_integer);
}

fn takes_ownership_and_gives_back(some_string: String) -> String {
    println!("{}", some_string);
    some_string
}

fn calculate_len(s: String) -> (String, usize) {
    let length = s.len();
    (s, length)
}
