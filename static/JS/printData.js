function printData()
{
   var divToPrint=document.getElementById("printScheduleTable");
   newWin= window.open("");
   newWin.document.write(divToPrint.outerHTML);
   newWin.print();
}
