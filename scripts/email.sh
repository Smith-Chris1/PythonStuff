filename=$(basename "$1")
directory=$(dirname "$1")
extension="${filename##*.}"
filename="${filename%.*}"
recipient='chris.smith@studiesweekly.com'
subject='File Uploaded to BluFire FTP'
body='Nate, I have uploaded a file: '$filename' to your ftp. Let me know if you have any issues or questions.'
mail -s $subject $recipient <<< $body
