#!/usr/bin/env python3
"""
Castle Building Planner using PAL MCP Server (Final Version)

This script uses the PAL MCP server's planner tool to create a comprehensive
plan for building a castle in Blender, including architecture, modeling techniques,
materials, lighting, rendering, and workflow organization.
"""

import json
import os
import sys
import asyncio

# Set UTF-8 encoding for stdout to handle Unicode characters
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

async def call_planner_tool():
    """Call the planner tool to create a castle building plan"""

    # Import necessary modules
    try:
        from server import configure_providers, TOOLS
        from utils.model_context import ModelContext
        from providers.registry import ModelProviderRegistry

        # Configure providers first
        configure_providers()
    except Exception as e:
        print(f"Error importing/configuring modules: {e}")
        return

    # Get the planner tool
    if "planner" not in TOOLS:
        print("Error: Planner tool not found in available tools")
        print(f"Available tools: {list(TOOLS.keys())}")
        return

    planner_tool = TOOLS["planner"]

    print("Creating comprehensive plan for building a castle in Blender...")
    print("=" * 70)

    try:
        # Get available models
        available_models = list(ModelProviderRegistry.get_available_models(respect_restrictions=True).keys())
        if not available_models:
            print("No models available. Please configure providers first.")
            return

        model_name = available_models[0]
        print(f"Using model: {model_name}")

        # Create model context
        model_context = ModelContext(model_name)

        # Execute all 8 steps in sequence
        steps = [
            # Step 1: Project overview
            {
                "step": "I need to create a comprehensive plan for building a detailed medieval castle in Blender. This will include: 1) Castle architecture and design elements (walls, towers, keep, gates, battlements), 2) Blender modeling techniques and workflow (blocking out, detailed modeling, modular design), 3) Materials and texturing strategy (stone, wood, metal, weathering), 4) Lighting and rendering setup (day/night cycles, atmospheric lighting), 5) Timeline and workflow organization (phased approach, asset management). The goal is to create a realistic, detailed castle that could be used for games, animation, or architectural visualization.",
                "step_number": 1,
                "total_steps": 8,
                "next_step_required": True,
            },
            # Step 2: Architecture
            {
                "step": "Based on the project scope, I'll now detail the castle architecture and design elements. This includes: 1) Main castle components (keep/citadel, curtain walls, corner towers, gatehouse, barbican, moat), 2) Architectural styles (Romanesque, Gothic, military fortress features), 3) Structural elements (battlements, crenellations, machicolations, arrow slits, murder holes), 4) Interior spaces (great hall, chambers, kitchens, chapel, dungeons), 5) Defensive features (drawbridge, portcullis, gate defenses). Each component needs historical accuracy and structural plausibility.",
                "step_number": 2,
                "total_steps": 8,
                "next_step_required": True,
            },
            # Step 3: Modeling techniques
            {
                "step": "Now planning the Blender modeling techniques and workflow: 1) Blocking out phase (primitive shapes, scale proportions, basic layout), 2) Modular modeling approach (create reusable assets like wall sections, towers, windows), 3) Detailed modeling techniques (subdivision surface, sculpting details, normal maps), 4) Optimization strategies (LOD levels, efficient topology, texture atlases), 5) Workflow organization (naming conventions, collection management, layering). The approach should balance detail with performance considerations.",
                "step_number": 3,
                "total_steps": 8,
                "next_step_required": True,
            },
            # Step 4: Materials and texturing
            {
                "step": "Planning the materials and texturing strategy: 1) Material categories (stone types - granite, limestone, sandstone; wood varieties - oak, pine; metals - iron, bronze), 2) Texture creation workflow (PBR materials, height maps, normal maps, ambient occlusion), 3) Weathering and aging techniques (cracks, moss, water stains, wear patterns), 4) UV unwrapping strategies (modular UVs, texture atlasing, efficient UV layout), 5) Shader setup (Blender Shader Editor, procedural materials, material nodes). Each material should reflect historical construction methods and environmental exposure.",
                "step_number": 4,
                "total_steps": 8,
                "next_step_required": True,
            },
            # Step 5: Lighting and rendering
            {
                "step": "Planning lighting and rendering setup: 1) Lighting scenarios (daylight - sun position, cloud shadows; nighttime - torches, moonlight; atmospheric - fog, volume lighting), 2) Light types and placement (area lights, point lights, spotlights, HDRI lighting), 3) Shadow configuration (shadow mapping, cascade shadows, contact shadows), 4) Rendering settings (Cycles vs Eevee, sampling settings, denoising), 5) Camera work (camera angles, focal lengths, depth of field, animation paths). The lighting should enhance the castle's mood and architectural features.",
                "step_number": 5,
                "total_steps": 8,
                "next_step_required": True,
            },
            # Step 6: Timeline and organization
            {
                "step": "Creating timeline and workflow organization: 1) Project phases (Research and Reference to Blocking Out to Detailed Modeling to Texturing to Lighting to Rendering to Post-Processing), 2) Time allocation per phase (realistic estimates based on complexity), 3) Asset management system (file organization, naming conventions, version control), 4) Quality control checkpoints (milestone reviews, technical validation), 5) Final deliverables (still renders, animation sequences, optimization for target platforms). The timeline should accommodate both creative exploration and technical requirements.",
                "step_number": 6,
                "total_steps": 8,
                "next_step_required": True,
            },
            # Step 7: Technical specifications
            {
                "step": "Technical specifications and optimization planning: 1) Polygon budget management (target poly counts for different components), 2) Texture optimization (resolution settings, compression formats, memory usage), 3) Level of Detail (LOD) strategy (multiple detail levels for different viewing distances), 4) Performance considerations (draw calls, material batching, physics collision), 5) Export settings (file formats, scale conventions, engine-specific requirements). This ensures the castle performs well in various applications while maintaining visual quality.",
                "step_number": 7,
                "total_steps": 8,
                "next_step_required": True,
            },
            # Step 8: Final summary
            {
                "step": "Final step: Comprehensive castle building plan summary. This plan covers all aspects of creating a detailed medieval castle in Blender: architectural design based on historical examples, systematic modeling workflow using modular techniques, comprehensive material and texturing strategies, professional lighting and rendering setups, realistic timeline with proper project organization, and technical optimization for various use cases. The plan provides a complete roadmap from concept to final renders, with specific techniques, tools, and workflows for each phase. Success criteria include historical accuracy, visual quality, technical performance, and efficient workflow management.",
                "step_number": 8,
                "total_steps": 8,
                "next_step_required": False,  # Final step
            },
        ]

        continuation_id = None

        # Execute each step
        for i, step_data in enumerate(steps, 1):
            print(f"\nSTEP {i}: {['Project Overview', 'Architecture', 'Modeling', 'Materials', 'Lighting', 'Timeline', 'Technical', 'Final Summary'][i-1]}")
            print("-" * 50)

            # Prepare parameters
            params = {
                "model": model_name,
                "_model_context": model_context,
                "_resolved_model_name": model_name,
                **step_data
            }

            # Add continuation_id if we have one
            if continuation_id:
                params["continuation_id"] = continuation_id

            try:
                result = await planner_tool.execute(params)

                if result and len(result) > 0:
                    response = result[0].text if hasattr(result[0], "text") else str(result[0])
                    print(f"Step {i} completed successfully")

                    # Parse response
                    try:
                        response_data = json.loads(response)
                        continuation_id = response_data.get("continuation_id")

                        # Handle different response types
                        status = response_data.get("status", "")
                        if status == "pause_for_deep_thinking":
                            print("Deep thinking pause - Complex plan analysis required")
                            # Continue automatically for this demo
                        elif status == "pause_for_planning":
                            print("Planning pause - Continuing to next step")

                        # Safely extract and display step content
                        step_content = response_data.get("step_content", "")
                        if step_content:
                            # Truncate for display and handle unicode safely
                            safe_content = step_content.encode('ascii', 'ignore').decode('ascii')[:200]
                            print(f"Content: {safe_content}...")

                        # Check if planning is complete
                        if response_data.get("planning_complete"):
                            print("\n" + "="*70)
                            print("COMPREHENSIVE CASTLE BUILDING PLAN COMPLETED!")
                            print("="*70)

                            plan_summary = response_data.get("plan_summary", "No summary available")
                            if plan_summary:
                                # Safely display summary
                                safe_summary = plan_summary.encode('ascii', 'ignore').decode('ascii')
                                print(f"\nPlan Summary:\n{safe_summary}")

                            # Display output instructions
                            if "output" in response_data:
                                output = response_data["output"]
                                if "instructions" in output:
                                    instructions = output["instructions"].encode('ascii', 'ignore').decode('ascii')
                                    print(f"\nFinal Instructions:\n{instructions}")

                            print(f"\nStatus: {response_data.get('status', 'Unknown')}")
                            print(f"Continuation ID: {continuation_id}")
                            print("\nNext Steps: You can now begin implementing the castle building plan!")

                            return  # Planning complete

                    except json.JSONDecodeError:
                        print(f"Raw response: {response[:200]}...")

                else:
                    print(f"Step {i} failed - no response received")
                    return

            except Exception as e:
                print(f"Error executing step {i}: {e}")
                continue

    except Exception as e:
        print(f"Error executing planner: {e}")
        import traceback
        traceback.print_exc()

def main():
    """Main function to run the castle building planner"""
    print("PAL MCP Server - Castle Building Planner")
    print("=" * 50)

    try:
        # Run the async planner
        asyncio.run(call_planner_tool())

    except KeyboardInterrupt:
        print("\n\nPlanning interrupted by user")
    except Exception as e:
        print(f"\nError running planner: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()