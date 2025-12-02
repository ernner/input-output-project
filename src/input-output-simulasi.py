import time


input_buffer = ""
output_buffer = ""


def cpu_read_input():
    global input_buffer
    user_input = input("Masukkan data (I/O): ")
    input_buffer = user_input
    return user_input


def cpu_process():
    global input_buffer, output_buffer
    time.sleep(0.5)
    output_buffer = input_buffer.upper()  
    return output_buffer


def cpu_output_data():
    global output_buffer
    print("Output dari sistem I/O:", output_buffer)


def main():
    print("=== SIMULASI SISTEM INPUT–OUTPUT SEDERHANA ===")

   
    data_in = cpu_read_input()

   
    processed = cpu_process()

  
    cpu_output_data()


if __name__ == "__main__":
    main()
