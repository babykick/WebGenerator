<!DOCTYPE html>
<html lang="en">
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   <title> 
      <%block name="title" />
   </title>
   
   <%block name="css" />

   <%block name="script" />

</head>

<body>
<div id="navigation">
   <div id="nav_bar">
     <%block name="navlist"/>
  </div> 
  <br>
   
  <span class="baner_text"> 
      ${page.title}
  </span>
  
  <span class="baner_text_sub">  
      ${page.subtitle}
  </span>
    
    
</div>  <!--navigation-->


<div id="wrapper2">
  <div id="wrapper">
     <div id="content-wrapper">
         <div id="content">
           <%block name="content"/>
   
         </div> <!--content-->
 
     </div> <!--content-wrapper-->
    
   
    <div id="sidebar-wrapper">
        <div id="sidebar">
            <img src="${imgdir}/coffee.jpg" width=180px />
           <%block name="sidebarinfo" />
        
        </div> <!--end of sidebar-->
        
    </div>  <!--end of sidebar-wrapper-->
   
  </div>  <!-- wrapper-->
  
  <div id="footer">
     <%block name="footer" />
   </div>
  
</div> <!-- wrapper2-->

</body>
</html>
