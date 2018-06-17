from collections import Counter
import random as rn
############# System configuration: (Python :3.5.2)###################
#### Cautios: Windows Machine path can be define as ('E:\\sphoorti\\assignment\\') ####
directory_location = "//home//assignment//"
Total_Reads = 100000
Number_of_bases = 50
In_Total = Total_Reads*Number_of_bases
Base_Count_Error_Rate = In_Total*.01
print(Base_Count_Error_Rate)
def base_change(line,bp):
    random_number = rn.randint(0,bp-1)
    original_base = line[random_number]
    bp_string = ['A','T','G','C']
    bp_string.remove(original_base)
    mutated_bp = rn.choice(bp_string)
    read_list = list(line)
    read_list[random_number]= mutated_bp
    read_after_mutation = "".join(read_list)
    print("Script is updating fastQ file with read: {0:s}".format(read_after_mutation))
    return (read_after_mutation)
########## Script start executing #######################
print("Second script execution starts...")
input_fastq_filepath = directory_location + 'output.fastq'
output_fastq_filepath = directory_location + 'output-witherror-rate.fastq'
input_fastq = open(input_fastq_filepath,"r+")
output_fastq = open(output_fastq_filepath,"w+")
line = input_fastq.readline()
cnt = 0
bp = 50
while line:
    new_line = line.strip()
    if(cnt < int(Base_Count_Error_Rate)):
        if(new_line.startswith("@m") and len(new_line)==8):
            output_fastq.write(line.strip() + '\n')
        elif(len(new_line)== bp and len(Counter(new_line))==4):
            new_read = base_change(new_line,bp)
            output_fastq.write(new_read + '\n')
        elif(len(new_line)== 1):
            output_fastq.write(new_line + '\n')
        else:
            output_fastq.write(new_line + '\n')
        cnt =cnt+1
    else:
        output_fastq.write(new_line + '\n')
    line = input_fastq.readline()

input_fastq.close()
output_fastq.close()
print("Second script executed successfully...")       
