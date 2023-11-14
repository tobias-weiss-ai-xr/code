// naive fibonacci

use std::io;

fn fib_first_attempt(x: u64) -> u64 {
    if x == 0 {
        0
    } else if x == 1 {
        1
    } else {
        fib(x - 1) + fib(x - 2)
    }
}

fn fib(x: u64) -> u64 {
    match x {
        0 => 0,
        1 => 1,
        _ => fib(x - 1) + fib(x - 2),
    }
}

fn main() {
    println!("Enter n to calculate the n-th Fibonacci number.");

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line.");
    let input_num: u64 = input.trim().parse().expect("Please input a number!");

    println!("The Fibonacci number is: {}", fib(input_num));

    // println!("The slow Fibonacci number is: {}", fib_first_attempt(input_num)); 
}