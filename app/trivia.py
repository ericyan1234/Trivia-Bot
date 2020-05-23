from discord.ext import commands
import discord
from datetime import datetime

class Trivia(commands.Cog):
    def __init__(self, client):
        self.client = client

    team_associations = {
        "TIG BIDDIES": [407649857252098048, 542200564964917259, 171803237043666944],
        "Brokestreet Kings": [711652918968844309, 711652918968844309, 711652918968844309],
        "STDs": [586786911994249230, 208744469720203264, 321836247330848768],
        "EZ Money": [386323964147793922, 133388200189231104, 262081474885320706],
        "Christ's Crusaders": [321484610821423116, 391829306713571339, 466111812035936256],
        "Jae's Jeans": [645451836857384970, 124668192948748288, 173210257202479104],
        "xXFaZeMiNeCrafTXx": [412371754988863488, 124673319520698372, 310240028078899201],
        "Indeed Indeed Joel Embiid": [451575960609882114, 354403176801239040]
    }
    channel_id = 713599817011560448
    record = False

    @commands.command(name = "start")
    @commands.has_permissions(administrator = True)
    async def start_record(self, ctx):
        """Begins recording submissions"""
        self.submissions = []
        self.record = True

    @commands.command(name = "end")
    @commands.has_permissions(administrator = True)
    async def stop_record(self, ctx):
        """Stops recording submissions"""
        channel = self.client.get_channel(self.channel_id)
        self.record = False
        embed = discord.Embed(title = "Submissions")
        for index, submission in enumerate(self.submissions):
            embed.add_field(name = f'{index + 1}. {submission["team_name"]}', value = f'Answer: {submission["answer"]} \nTimestamp: {submission["timestamp"]}', inline = False)
        await channel.send(embed = embed)

    @commands.command(name = "answer")
    async def trivia_submission(self, ctx, *, submission):
        """Forwards answer to centralized chat"""
        if self.record:
            if isinstance(ctx.channel, discord.DMChannel):
                member = ctx.author.id
                for team, members in self.team_associations.items():
                    if member in members:
                        break
                already_submitted = [1 for record in self.submissions if record["team_name"] == team]
                if not already_submitted:
                    self.submissions.append({"team_name": team, "answer": submission, "timestamp": datetime.now().strftime('%H:%M:%S.%f')[:-4]})


def setup(client):
    client.add_cog(Trivia(client))
