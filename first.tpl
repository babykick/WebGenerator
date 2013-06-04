<%inherit file="base.html" />

<%block name="title">
   first page analysis
</%block>
 
 
<%block name="content">
  <div class="post"> 
      <h2><a href="#"> First page analysis</a><br></h2>
      <p> 
            <%include file="first_sol.txt"/>
      </p>
               
  </div>  
 

</%block>


