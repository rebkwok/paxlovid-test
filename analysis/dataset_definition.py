from ehrql import create_dataset, codelist_from_csv
from ehrql.tables.beta.core import medications
from ehrql.tables.beta.tpp import practice_registrations

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--start")
parser.add_argument("--end")
args = parser.parse_args()


# Medications of interest
paxlovid_GP_codes = codelist_from_csv("codelists/user-bangzheng-paxlovid-dmd.csv", column="code")

dataset = create_dataset()

# Find first prescription in July 2023
paxlovid_prescriptions = medications.where(
  medications.dmd_code.is_in(paxlovid_GP_codes)
).where(
  medications.date.is_on_or_between(args.start, args.end)
).sort_by(medications.date).first_for_patient()

# Define population as patients registered with a practice on the date of their prescription
registered = practice_registrations.for_patient_on(paxlovid_prescriptions.date)
dataset.define_population(registered.exists_for_patient())

# Output date of prescription
dataset.date_treated = paxlovid_prescriptions.date
