use std::io;

const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;

fn main() {
    println!("3 hours: {}", THREE_HOURS_IN_SECONDS);
    let x = 5;
    println!("The value of x is: {}", x);
    let x = x + 1;
    {
        let x = x * 2;
        println!("The value of the inner scope is: {}", x);
    }
    println!("The value of x is: {}", x);

    let _guess: u32 = "42".parse().expect("Not a number!");
 
    let _t = true;
    let _f: bool = false;

    let _c = 'z';
    let _z = 'ℤ';
    let heart_eyed_cat = '😻';
    println!("{}", heart_eyed_cat);

    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (_x, _y, _z) = tup; // pattern matching

    let _six_point_four = tup.1; // index
    let _one = tup.2;

    let _arr = [1, 2, 3];
    let _arr: [i32; 3] = [1, 2, 3]; // typed array

    let _arr = [42; 3]; // repeat 42 three times
    for elem in _arr {
        println!("The answer is {}.", elem);
    }

    let mut idx = String::new();

    println!("Please enter an index");

    io::stdin()
        .read_line(&mut idx)
        .expect("Failed to read line");
    
        let idx: usize = idx
            .trim()
            .parse()
            .expect("Index was not a number");

    println!("Arr position {}: {}", idx, _arr[idx]);
}
