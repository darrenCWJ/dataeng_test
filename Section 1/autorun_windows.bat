PowerShell

$action = New-ScheduledTaskAction -Execute 'dataset_cleaning.py'
$trigger = New-ScheduledTaskTrigger -Daily -At 1am
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "dataset_cleaning"