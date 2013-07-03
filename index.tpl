<%inherit file="base.html" />

<%block name="title">
    ${name}: ${courseInfo}
</%block>
 
<%block name="navlist">
   <ul>
        <li class="page_item"><a href="index.html">Home</a></li>
        <li class="page_item page-item-links"><a href="first.html" title="first">First</a></li>
        <li class="page_item page-item-text"><a href="mailto:youremailaddress" title="email">Jing Tao</a></li>
  </ul>

</%block> 
 
<%block name="content">
  <div class="post"> 
      <h2><a href="#"> ${articleTitle}</a><br></h2>
      <p> 
           ## <%include file=${includeFile}/>
           ${articleContent}
      </p>
               
  </div>  
 

</%block>

<%block name="sidebarinfo">
   <ul>
     <li> Student Name: ${name} </li>
   </ul>
 
</%block>


