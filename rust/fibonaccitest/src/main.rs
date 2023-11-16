// naive fibonacci

use crate::fibo::fib;
use std::io;

pub mod fibo;

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
