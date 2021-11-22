import React, { useState, useRef } from 'react';
import ReactFlow, {
  ReactFlowProvider,
  addEdge,
  removeElements,
  MiniMap,
  Controls,
  Background,
  updateEdge
} from 'react-flow-renderer';

import Sidebar from './Sidebar';
import "./images.css";
import './App.css';

const initialElements = [
  {
    id: '1',
    type: 'input',
    data: { label: 'process_start' },
    position: { x: 250, y: 5 }
  },
];

let id = 0;
const getId = () => `dndnode_${id++}`;


const style = {
  background: '#485563',
  width: '100%',
  height: 800,
}

const App = () => {
  const reactFlowWrapper = useRef(null);
  const [reactFlowInstance, setReactFlowInstance] = useState(null);
  const [elements, setElements] = useState(initialElements);
  const onConnect = (params) => setElements((els) => addEdge(params, els));
  const onEdgeUpdate = (oldEdge, newConnection) =>
  setElements((els) => updateEdge(oldEdge, newConnection, els));
  const onElementsRemove = (elementsToRemove) =>
    setElements((els) => removeElements(elementsToRemove, els));

  const onLoad = (_reactFlowInstance) =>
    setReactFlowInstance(_reactFlowInstance);

  const onDragOver = (event) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
  };

  const onDrop = (event) => {
    event.preventDefault();

    const reactFlowBounds = reactFlowWrapper.current.getBoundingClientRect();
    const type = event.dataTransfer.getData('application/reactflow');
    const position = reactFlowInstance.project({
      x: event.clientX - reactFlowBounds.left,
      y: event.clientY - reactFlowBounds.top,
    });
    const newNode = {
      id: getId(),
      className: `${type}`,
      type: 'node',
      position,
      data: { label: `${type}` }
    };

    setElements((es) => es.concat(newNode));
  };

  const CustomEdgeComponent = {
    type: 'arrow' | 'arrowclosed'
  }

  return (
    <div className="dndflow">
      <Sidebar />
      <ReactFlowProvider>
        <div className="reactflow-wrapper" ref={reactFlowWrapper}>
          <ReactFlow
            style={style}
            edgeTypes={{ special: CustomEdgeComponent }}
            elements={elements}
            onConnect={onConnect}
            onElementsRemove={onElementsRemove}
            onEdgeUpdate={onEdgeUpdate}
            onLoad={onLoad}
            onDrop={onDrop}
            onDragOver={onDragOver}
            snapToGrid={true}
            snapGrid={[15,15]}
          >
            <MiniMap
              nodeStrokeColor={(n) => {
                if (n.style?.background) return n.style.background;
                if (n.type === 'input') return '#0041d0';
                if (n.type === 'node') return '#ff0072';
                if (n.type === 'arrowclosed') return '#1a192b';

                return '#eee';
              }}
              nodeColor={(n) => {
                if (n.style?.background) return n.style.background;
                return '#fff';
              }}
              nodeBorderRadius={2}
            />
            <Background color="#aaa" gap={16} />
            <Controls />
          </ReactFlow>
        </div>
      </ReactFlowProvider>
    </div>
  );
};

export default App;