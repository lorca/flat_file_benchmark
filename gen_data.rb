#
# generate a data file
#
# do ruby gen_data.rb > input/mydata.csv
#

user_id=1
for user_id in (1..10000)
 payments = (rand * 1000).to_i
 for user_payment_id in (1..payments)
   payment_id = user_id.to_s + user_payment_id.to_s
   payment_amount = "%.2f" % (rand * 30);
   is_card_present = "N"
   created_at = (rand * 10000000).to_i
   if payment_id.to_i % 3 == 0
    is_card_present = "Y"
   end
   puts [user_id, payment_id, payment_amount, is_card_present, created_at].join("\t")
 end
end

