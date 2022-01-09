use std::io;
use rand::Rng;

fn main() {
    println!("Guess a number!");
    println!("Please enter your number:");

    let secret_number = rand::thread_rng().gen_range(1..101);
    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {}", guess);
}