import random as rn
############# System configuration: (Python :3.5.2)###################
#### Cautios: Windows Machine path can be define as ('E:\\sphoorti\\assignment\\') ####
directory_location = '//home//assignment//'
def random_read_generator(line,bp,overall_bp,start,end,unique_id):
    random_number = rn.randint(start,end)
    start_read = len(overall_bp)-80+start
    end_read = len(overall_bp)-80+start+bp
    read_string = line[random_number:random_number+bp]
    target_file.write(str(unique_id) + "\t" + str(start_read) + "\t" + str(end_read) + "\n")
    return read_string
def unique_id_generator(unique_id):
    identifier = "@m"+str(unique_id+1)
    unique_id += 1
    return (identifier,unique_id)
def writing_into_fastq(unique_identifier,read,ASCII_character,bp,fastq_file):
    quality_character_list = rn.sample(ASCII_character,bp)
    quality_character_string = ''.join(quality_character_list)
    fastq_file.write(unique_identifier + '\n')
    fastq_file.write(read + '\n')
    fastq_file.write("+" + '\n')
    fastq_file.write(quality_character_string + '\n')
    print("Fastq file is being updated for id {0:s}".format(unique_identifier))
#Before to run: File reading (define filenames)
print("First script execution starts...")
input_fasta_filepath = directory_location +'genome.fna' #### genome file #####
output_fastq_filepath = directory_location + 'output.fastq' #### output fastq file ####
ASCII_table = directory_location + 'ASCII-table.txt' #### ASCII string for dummy quality score #######
target_region = directory_location + 'TargetQC.bed' #### Target Region track #######
fastq_file= open(output_fastq_filepath,"w+")
target_file = open (target_region,"w+")
target_file.write("Chromosome" + "\t" + "Start" + "\t" + "End" + "\n")
ASCII_file = open(ASCII_table,"r")
ASCII_character = list(ASCII_file.readline())
unique_id = 300000 # Unique identifier for each read in Fastq file
number_of_reads = 100000
bp = 50
#Things to know [Logic] :one line generates two reads
with open(input_fasta_filepath) as fp:  
   line = fp.readline()
   read_cnt = 0
   while line:
       new_line = line.strip()
       if(new_line.startswith(">")):
           overall_bp = ""
       if(len(new_line)==80 and (not new_line.startswith(">"))): #initial check for fasta file reading 
           overall_bp = overall_bp + new_line
           unique_identifier,unique_id = unique_id_generator(unique_id)
           read_one = random_read_generator(new_line,bp,overall_bp,1,15,unique_id) #First read
           writing_into_fastq(unique_identifier,read_one,ASCII_character,bp,fastq_file) # calling function for fastq output
           unique_identifier,unique_id = unique_id_generator(unique_id)
           read_second = random_read_generator(new_line,bp,overall_bp,16,30,unique_id) #Second read
           writing_into_fastq(unique_identifier,read_second,ASCII_character,bp,fastq_file)
           if(read_cnt < number_of_reads-2):
               read_cnt += 2
           else:
               break
       line = fp.readline()
fp.close()
fastq_file.close()
ASCII_file.close()
target_file.close()
print("First script executed successfully...")
