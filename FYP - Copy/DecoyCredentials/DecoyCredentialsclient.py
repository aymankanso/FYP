import asyncio
import asyncssh

async def connect_ssh():
    async with asyncssh.connect('localhost') as conn:
        result = await conn.run('ls')
        print(result.stdout)

# Run the SSH client
asyncio.run(connect_ssh())

