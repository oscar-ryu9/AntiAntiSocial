import generateDummyNames
import AAS_IO
import AI



if __name__ == "__main__":

    # students = AAS_IO.importDummyNames()
    # print(AI.preprocess(students[22],students[5]))
    ai = AI.AAS_AI()
    ai.load_from_file_and_train()




