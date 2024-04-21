import React, { useRef, useEffect } from 'react'

const {tableau} = window;

function TableauEmbed() {
  const ref = useRef(null);
  const url = "https://public.tableau.com/views/RealHack/Dashboard1?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link";

  function initViz() {
    new tableau.Viz(ref.current, url);
  }

  useEffect(() =>{
    initViz();
  }, []);

  return (
    // <div>tableau</div>
    <div ref={ref}></div>
  )
}

export default TableauEmbed;