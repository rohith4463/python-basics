"""a={"rohith":{"roll number":231,"maths":80,"physics":87,"hindi":99},
   "pooja":{"roll number":232,"maths":88,"physics":70,"hindi":95},
   "sai":{"roll number":233,"maths":86,"physics":75,"hindi":92}}
##print((a["rohith"]["maths"]+a["rohith"]["physics"]+a["rohith"]["hindi"]),type(a))

for name,details in a.items():
    total=details["physics"]+details["maths"]+details["hindi"]
    print(f"{name} -> {total}")"""



student_data = {"saik":{"roll number":432,"gender":"male","marks":[89,79,65,45,23]},
                "mai":{"roll number":433,"gender":"female","marks":[85,75,55,45,83]},
                "lee":{"roll number":433,"gender":"male","marks":[98,70,76,45,93]}}
for name,details in student_data.items():
    total=sum(details["marks"])
    print(f"{name} has scored {total} marks")

